$(document).ready(function() {

    $('#addButton').on('click', function(event) {
        event.preventDefault();
        const task_title = $('#todo_task').val();
        const list = $('#incomplete_tasks');

        $.post("/todolist/add", { task_title: task_title }, function(data) {
            var task_id = data.id
            var task_title = data.task_title
            const item =
            '<li class="col-md-10 todo-item" id=id_item_' + task_id + ' task_id=' + task_id + '>' + 
                '<div class="col-md-1 form-group form-check">' +
                    '<input type="checkbox" class="form-check-input">' +
                '</div>' +
                '<div class="col-md-9">' +
                    '<label id=id_title_' + task_id + '>' + task_title + '</label>' +
                '</div>' +
                '<div class="col-md-1">' +
                    '<span class="editButton"><i class="fas fa-pencil-alt"></i></span>' +
                '</div>' +
                '<div class="col-md-1">' +
                    '<span class="deleteButton"><i class="fas fa-trash-alt"></i></span>' +
                '</div>' +
            '</li>';

            list.prepend(item);
        });
        $('#add_todo_task')[0].reset();
    });


    $('.todo-list').on('click', ".editButton", function(event) {
        event.preventDefault();
        const task_id = $(this).closest("li").attr('task_id');
        var task_title = $('#id_title_'+task_id).text();
        $("#id_item_"+task_id).empty();
        $("#id_item_"+task_id).html(
            '<form class="updateForm" id=form_task_' + task_id + '>' +
                '<input type="text" name="todo_task" id=todo_task_' + task_id + ' value=' + task_title + '>' +
                '<button type="button" class="btn btn-primary updateButton" id=button_task_' + task_id + '>Update</button>' + 
            '</form>'
            );
    });


    $('.todo-list').on('click', ".updateButton", function(event) {
        event.preventDefault();
        const task_id = $(this).closest("li").attr('task_id');
        const task_title = $('#todo_task_'+task_id).val();

        $.ajax({
            type: 'POST',
            url: "/todolist/update",
            data: { task_id: task_id, task_title: task_title },
            dataType: "text",
        });            

        $("#id_item_"+task_id).empty();
        $("#id_item_"+task_id).html(
                '<div class="col-md-1 form-group form-check">' +
                    '<input type="checkbox" class="form-check-input">' +
                '</div>' +
                '<div class="col-md-9">' +
                    '<label id=id_title_' + task_id + '>' + task_title + '</label>' +
                '</div>' +
                '<div class="col-md-1">' +
                    '<span class="editButton"><i class="fas fa-pencil-alt"></i></span>' +
                '</div>' +
                '<div class="col-md-1">' +
                    '<span class="deleteButton"><i class="fas fa-trash-alt"></i></span>' +
                '</div>');
    });

    
    $('.todo-list').on('change', ":checkbox", function(event) {
        event.preventDefault();
        const task_id = $(this).closest("li").attr('task_id');
        const list_incomplete = $('#incomplete_tasks');
        const list_complete = $('#completed_tasks');
        const element = $("#id_item_"+task_id);

        if(this.checked) {
            list_complete.prepend(element);

            $.ajax({
                type: 'POST',
                url: "/todolist/status",
                data: { task_id: task_id, task_complete: 'True' },
                dataType: "text",
            });

        } else {
            list_incomplete.prepend(element);

            $.ajax({
                type: 'POST',
                url: "/todolist/status",
                data: { task_id: task_id, task_complete: 'False' },
                dataType: "text",
            });

        }
    });


    $('.todo-list').on('click', ".deleteButton", function (event) {
        event.preventDefault();
        const task_id = $(this).closest("li").attr('task_id');
        
        $.ajax({
            type: 'POST',
            url: "/todolist/delete",
            data: {task_id: task_id},
            dataType: "text",
        });
        
        $("#id_item_"+task_id).remove();
    });

});
