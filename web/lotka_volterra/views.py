from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from lotka_volterra.models import LVDiffEqSolution
from lotka_volterra.forms import SubmitCalculationForm
from lotka_volterra.calc.lokta_voltera import draw_plot
from django.contrib.auth.decorators import login_required

import os
from Webapp import settings
from lotka_volterra.scripts.excel_utils import write_to_excel


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def add_calculation(request):
    if request.method == 'POST':
        form = SubmitCalculationForm(request.POST)
        if form.is_valid():
            calc = form.save(commit=False)
            calc.user = request.user
            calc.save()
            return redirect('/lotka_volterra/calc_result/{}'.format(calc.id))
    else:
        form = SubmitCalculationForm()

    return render(request, 'lotka_volterra/add_calculation.html', {'form': form})


@login_required(login_url='/accounts/login/')
def calculation_result(request, calc_id):
    context_dict = {}
    try:
        calculation = LVDiffEqSolution.objects.get(id=int(calc_id))
        draw_plot(calculation.init_param_a,
                  calculation.init_param_b,
                  calculation.init_param_c,
                  calculation.init_param_d,
                  calculation.init_condition_x,
                  calculation.init_condition_y,
                  str(calculation.id)
                  )
        context_dict['calc_id'] = calculation.id
        context_dict['calculation'] = calculation
        context_dict['g1'] = 'graphs/rabbits_and_foxes_1_{}.png'.format(calculation.id)
        context_dict['g2'] = 'graphs/rabbits_and_foxes_2_{}.png'.format(calculation.id)
        context_dict['g3'] = 'graphs/rabbits_and_foxes_3_{}.png'.format(calculation.id)
        context_dict['report_link'] = '/lotka_volterra/calc_report/{}'.format(calculation.id)
        print(context_dict)

    except LVDiffEqSolution.DoesNotExist:
        pass

    return render(request, 'lotka_volterra/calc_result.html', context_dict)


@login_required(login_url='/accounts/login/')
def my_calculations(request):
    context_dict = {}
    try:
        calculations = LVDiffEqSolution.objects.all().filter(user=request.user)
        context_dict['calculations'] = calculations
    except LVDiffEqSolution.DoesNotExist:
        pass
    return render(request, 'lotka_volterra/calc_history.html', context_dict)


@login_required(login_url='/accounts/login/')
def get_xls_for_calc(request, calc_id):
    try:
        calculation = LVDiffEqSolution.objects.get(id=int(calc_id))
        write_to_excel({
            'init_param_a': calculation.init_param_a,
            'init_param_b': calculation.init_param_b,
            'init_param_c': calculation.init_param_c,
            'init_param_d': calculation.init_param_d,
            'init_condition_x': calculation.init_condition_x,
            'init_condition_y': calculation.init_condition_y,
            'calc_id': str(calculation.id)
        })
    except LVDiffEqSolution.DoesNotExist:
        pass

    excel_doc_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'excel_reports') + '/report_{}.xlsx'.format(calc_id)

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'

    with open(excel_doc_path, mode='rb') as file:
        xlsx_data = file.read()

    response.write(xlsx_data)
    return response
