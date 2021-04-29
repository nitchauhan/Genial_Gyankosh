$(document).ready(function() {
//toastr.info('Page Loaded!');
    display_toastr();
  });


function display_toastr()
{
    var a = document.getElementById('auth_flag');
//    alert(a.value);
    if (a.value == '1')
    {
//        toastr.options.timeOut = 1500; // 1.5s
        toastr.error('Wrong Password / UserName');
    }

}