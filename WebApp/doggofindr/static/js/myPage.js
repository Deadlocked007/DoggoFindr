
$(document).ready(function(){
  $(".deleteImg").click(function(){
    var imgId = this.id
    $.fn.deleteImg(imgId)
    $("#imageForm").submit()
  })
})
$.fn.deleteImg = function(imgId){
  $.ajax({
    url:'/deleteImg',
    type:'GET',
    data:{
      'action':1,
      'imgId':imgId,

    },
    dataType:'json',
    success: function(data){

      //alert(data.grayImageList[0])
    }
  })
}
