import os
import xlsxwriter

from Webapp import settings


def write_to_excel(calc_data):
    excel_doc_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'excel_reports') + '/report_{}.xlsx'.format(calc_data['calc_id'])
    graph_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'graphs') + '/rabbits_and_foxes_{}_{}.png'
    try:
        os.remove(excel_doc_path)
    except OSError:
        pass
    workbook = xlsxwriter.Workbook(excel_doc_path)

    worksheet_s = workbook.add_worksheet("Результат")
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    title_text = u"{0} {1}".format("Результат рассчета ", calc_data['calc_id'])
    worksheet_s.merge_range('B2:H2', title_text, title)

    worksheet_s.set_column('A:A', 40)

    worksheet_s.write(4, 0, "Коэф. естественного повышения качества", header)
    worksheet_s.write(4, 1, calc_data['init_param_a'], header)

    worksheet_s.write(5, 0, "Коэф. субсидий", header)
    worksheet_s.write(5, 1, calc_data['init_param_c'], header)

    worksheet_s.write(6, 0, "Коэф. жесткости регулирования", header)
    worksheet_s.write(6, 1, calc_data['init_param_b'], header)

    worksheet_s.write(7, 0, "Показатель безопасности транспортной услуги", header)
    worksheet_s.write(7, 1, calc_data['init_param_d'], header)

    worksheet_s.write(8, 0, "Начальное качество транспортной услуги", header)
    worksheet_s.write(8, 1, calc_data['init_condition_x'], header)

    worksheet_s.write(9, 0, "Начальная жесткость регулирования", header)
    worksheet_s.write(9, 1, calc_data['init_condition_y'], header)

    worksheet_s.insert_image('E5', graph_path.format("1", calc_data['calc_id']), {'x_scale': 0.5, 'y_scale': 0.5})
    worksheet_s.insert_image('E25', graph_path.format("2", calc_data['calc_id']), {'x_scale': 0.5, 'y_scale': 0.5})
    worksheet_s.insert_image('E45', graph_path.format("3", calc_data['calc_id']), {'x_scale': 0.5, 'y_scale': 0.5})

    workbook.close()
    return excel_doc_path