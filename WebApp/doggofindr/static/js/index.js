$(document).ready(function(){
  $("#uploadImage").click(function(){
    $("#imageForm").submit()
  })
  $("#findBreed").click(function(){
    $.fn.findBreed()
  })
})

$.fn.findBreed = function(){
  $.ajax({
    url:'/grey/',
    type:'GET',
    data:{
      'action':1,
    },
    dataType:'json',
    success: function(data){
      alert(data.message)
      //alert(data.grayImageList[0])
      $("#grayImageDiv").append("<img class='mySlides reportImage' src='"+data.grayImageList[0]+"'/>");
    }
  })
}
