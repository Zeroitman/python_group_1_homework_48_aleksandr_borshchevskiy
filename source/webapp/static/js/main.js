// function addOrderFoodSuccess(response, status) {
//     const orderFoodDeleteURL = "{% url 'webapp:order_food_delete' 0 %}";
//     console.log(response);
//     console.log(status);
//     let newFoodTr = $('#order_food_template').clone();
//     newFoodTr.removeAttr('id');
//     newFoodTr.find('.order_food_name').text(response.food_name);
//     newFoodTr.find('.order_food_amount').text(response.amount);
//     newFoodTr.find('.order_food_btn').attr('href', orderFoodDeleteURL.replace('0', response.pk));
//     $('#order_food_list').append(newFoodTr);
//     $('#food_edit_modal').modal('toggle');
// }
//
// function submitOrderFoodError(response, status) {
//     console.log(response);
//     console.log(status);
// }
//
// function addOrderFood() {
//     let url = $('#food_form').attr('action');
//     let data = {
//         food: $('#id_food').val(),
//         amount: $('#id_amount').val(),
//         csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//     };
//     $.ajax({
//         url: url,
//         method: 'POST',
//         data: data,
//         success: addOrderFoodSuccess,
//         error: submitOrderFoodError
//     });
// }
//
// $('#food_submit').on('click', function (e) {
//     $('#food_form').submit();
// });
// $('#food_form').on('submit', function (e) {
//     e.preventDefault();
//     addOrderFood();
// });

//------------------------------------------------------------------

function onCreateSuccess(response, status) {
    console.log(response);
    console.log(status);
    let newFoodLi = $('<li></li>');
    let foodNameSpan = $('<span></span>')
        .attr('id', 'order_food_name_' + response.pk)
        .data('food_pk', response.food_pk)
        .text(response.food_name);
    let foodAmountSpan = $('<span></span>')
        .attr('id', 'order_food_amount_' + response.pk)
        .text(response.amount);
    let editLink = $('<a></a>')
        .addClass('edit_link')
        .attr('href', response.edit_url)
        .data('pk', response.pk)
        .text('Изменить')
        .click(onOrderFoodUpdate);
    let deleteLink = $('<a></a>')
        .attr('href', '#')
        .text('Удалить');

    newFoodLi
        .attr('id', 'order_food_' + response.pk)
        .append(foodNameSpan)
        .append(document.createTextNode(': '))
        .append(foodAmountSpan)
        .append(document.createTextNode(' шт. ('))
        .append(editLink)
        .append(document.createTextNode(' / '))
        .append(deleteLink)
        .append(document.createTextNode(')'));

    $('#order_food_list').append(newFoodLi);

    $('#food_edit_modal').modal('hide');
}

function onUpdateSuccess(response, status) {
    console.log(response);
    console.log(status);
    let pk = response['pk'];
    let food_name_span = $('#order_food_name_' + pk);
    food_name_span.text(response.food_name);
    food_name_span.data('food_pk', response.food_pk);
    $('#order_food_amount_' + pk).text(response.amount);
    $('#food_edit_modal').modal('hide');
}

function onFormSubmitError(response, status) {
    console.log(response);
    console.log(status);
    if (response.errors) {
        $('#food_form_errors').text(response.errors.toString());
    }
}
function orderFoodFormSubmit(success) {
    let url = $('#food_form').attr('action');
    let data = {
        food: $('#id_food').val(),
        amount: $('#id_amount').val(),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
    };
    $.ajax({
        url: url,
        method: 'POST',
        data: data,
        success: success,
        error: onFormSubmitError
    });
}
function onOrderFoodCreate(event) {
    event.preventDefault();
    $("#food_edit_modal .modal-title").text('Добавить блюдо');
    $("#food_submit").text('Добавить');
    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));
    $('#id_food').val('');
    $('#id_amount').val('');
    foodForm.off('submit');
    foodForm.on('submit', function (e) {
        e.preventDefault();
        orderFoodFormSubmit(onCreateSuccess);
    });
    $('#food_edit_modal').modal('show');
}

function onOrderFoodUpdate(event) {
    event.preventDefault();
    $("#food_edit_modal .modal-title").text('Изменить блюдо');
    $("#food_submit").text('Изменить');
    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));
    let foodPk = $(this).data('pk');
    let foodName = $('#order_food_name_' + foodPk);  // '#order_food_name_1'
    let foodAmount = $('#order_food_amount_' + foodPk);  // '#order_food_amount_1'
    $('#id_food').val(foodName.data('food_pk'));
    $('#id_amount').val(foodAmount.text());
    foodForm.off('submit');
    foodForm.submit(function (event) {
        event.preventDefault();
        orderFoodFormSubmit(onUpdateSuccess);
    });
    $('#food_edit_modal').modal('show');
}

window.addEventListener('load', function () {
    $('#food_submit').on('click', function (e) {
        $('#food_form').submit();
    });
    $("#order_food_add_link").click(onOrderFoodCreate);
    $('#order_food_list .edit_link').click(onOrderFoodUpdate);
});


