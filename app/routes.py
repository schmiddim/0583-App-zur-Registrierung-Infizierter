def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('person_create', '/person_info')
    config.add_route('person_status', '/status')

    config.add_route('admin_overview', '/admin')
    config.add_route('admin_overview_json', '/admin_json')
    config.add_route('admin_edit_case', '/admin/edit')

    config.add_route("json_person_status", 'api/v1/status/{email}/{case_number}')
    config.add_route("json_person_create", 'api/v1/create')