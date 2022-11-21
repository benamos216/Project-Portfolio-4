//Displays message confirming user wants to delete item
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
});