frappe.views.calendar['Appointment'] = {
    field_map: {
        start: 'start_date',
        end: 'end_date',
        id: 'name',
        title: 'client_name',
        status: 'status'
    },
    order_by: 'start_date',
    get_events_method: 'scheduling_system_app.scheduling_system_app.calendar.get_events'
};
