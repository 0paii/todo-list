$(document).ready(function () {
    $(".checkbox_complete").change(function () {
        let id = $(this).attr('data-id')
        $.ajax({
            url: `main/task/change_complete/${id}/`,
            type: "POST",
            data: {
                status: this.checked,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (result) {
                console.log(result);
            },
            error: function (error) {
                console.log(error);
            }
        });

    });
});