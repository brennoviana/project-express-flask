def format_date(value):
    if value is None:
        return "Data não disponível"
    return value.strftime('%d/%m/%Y')

def register_filters(app):
    app.template_filter('formatdate')(format_date)
