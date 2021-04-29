function zz(a)
{

    var count = a.value;
    var arr =["bc1","bc2","bc3","bc4","bc5"];
    var i;
    for(i=0;i<a.value;i++)
    {
        var temp = document.getElementById(arr[i]);
        temp.style.display="block";
    }

    document.getElementById("back_camera1").focus();
}

function yy(a)
{

    var count = a.value;
    var arr =["fc1","fc2","fc3","fc4","fc5"];
    var i;
    for(i=0;i<a.value;i++)
    {
        var temp = document.getElementById(arr[i]);
        temp.style.display="block";
    }

    document.getElementById("front_camera1").focus();
}

