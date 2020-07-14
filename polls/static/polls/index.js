

$(document).ready(function() {
console.log("Đã kết nối được với file index.js")


$('#vertical').lightSlider({
      loop:true,
      auto:true,
      item:1,
      vertical:true,
      thumbItem:5,
      thumbMargin:4,
      slideMargin:0
    });

/* -----------chức năng nhấn nút back thì quay trở lại trang trước đó */
$("#back_btn").click(function (){
  parent.history.back();
		return false;
  console.log("đã back")
});
/* End chức năng nhấn nút back thì quay trở lại trang trước đó */

new WOW().init();
/* ------------tính năng xử xí footer xuất hiện cho hợp lý ở phần search */
var vitri = $('.footer').offset();
  if(vitri.top <= 600){
       $('.empty_search').removeClass('diableDiv');
       console.log("vị trí của footer nhỏ hơn 500px");
  }
  else{
      $('.empty_search').addClass('diableDiv');
      console.log("vị trí của footer lớn hơn 500px");
  }
/* End tính năng xử xí footer xuất hiện cho hợp lý ở phần search */
/* ---------------xử lý cho slide */
//    $("#content-slider").lightSlider({
//        loop:true,
//        keyPress:true,
//        auto:true,
//        pager: true,
//        responsive : [
//            {
//                breakpoint:450,
//                settings: {
//                    item:2,//khi resposive thì chỉ hiện 2 slide/lần trượt
//                    slideMove:1,
//                    slideMargin:6,
//                  }
//            },
//            {
//                breakpoint:350,
//                settings: {
//                    item:1,//khi resposive thì chỉ hiện 1 slide/lần trượt
//                    slideMove:1,
//                    slideMargin:6,
//                  }
//            }
//        ]
//
//    });
/* end xử lý cho slide */



//--------------xử lý nút kéo lên trang đầu
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.on_top').fadeIn();
        } else {
            $('.on_top').fadeOut();
        }
    });
    $('.on_top').click(function(){
        $("html").animate({ scrollTop: 0 },600);
        return false;
    });
//end xử lý nút kéo lên trang đầu


///* xử lý cho wow.js để nó lặp lại liên tục khi mình rê chuột tới phần tử chứa wow.js */
//window.addEventListener('scroll', function(e) {
//
//    if( $(window).scrollTop() < 5) {
//        $('.wow').removeClass('animated');
//        $('.wow').removeAttr('style');
//        new WOW().init();
//    }
// });
// /* End lý cho wow.js để nó lặp lại liên tục khi mình rê chuột tới phần tử chứa wow.js */

/* -------------Xử lý Chức năng Search Suggestion---------------  */
function KhongDau(str){ //hàm chuyển chữ có dẫu thành ko dấu
	if (typeof str != 'string')
		return null;

	str = str.replace(/(á|à|ả|ã|ạ|ă|ắ|ằ|ẳ|ẵ|ặ|â|ấ|ầ|ẩ|ẫ|ậ)/g, 'a');
	str = str.replace(/(A|Á|À|Ả|Ã|Ạ|Ă|Ắ|Ằ|Ẳ|Ẵ|Ặ|Â|Ấ|Ầ|Ẩ|Ẫ|Ậ)/g, 'A');
	str = str.replace(/đ/g, 'd');
	str = str.replace(/Đ/g, 'D');
	str = str.replace(/(é|è|ẻ|ẽ|ẹ|ê|ế|ề|ể|ễ|ệ)/g, 'e');
	str = str.replace(/(É|È|Ẻ|Ẽ|Ẹ|Ê|Ế|Ề|Ể|Ễ|Ệ)/g, 'E');
	str = str.replace(/(í|ì|ỉ|ĩ|ị)/g, 'i');
	str = str.replace(/(Í|Ì|Ỉ|Ĩ|Ị)/g, 'I');
	str = str.replace(/(ó|ò|ỏ|õ|ọ|ô|ố|ồ|ổ|ỗ|ộ|ơ|ớ|ờ|ở|ỡ|ợ)/g, 'o');
	str = str.replace(/(Ó|Ò|Ỏ|Õ|Ọ|Ô|Ố|Ồ|Ổ|Ỗ|Ộ|Ơ|Ớ|Ờ|Ở|Ỡ|Ợ)/g, 'O');
	str = str.replace(/(ú|ù|ủ|ũ|ụ|ư|ứ|ừ|ử|ữ|ự)/g, 'u');
	str = str.replace(/(Ú|Ù|Ủ|Ũ|Ụ|Ư|Ứ|Ừ|Ử|Ữ|Ự)/g, 'U');
	str = str.replace(/(ý|ỳ|ỷ|ỹ|ỵ)/g, 'y');
	str = str.replace(/(Ý|Ỳ|Ỷ|Ỹ|Ỵ)/g, 'Y');

	str = str.replace(/[^a-zA-Z0-9_-]/g, '-');

	while (str.length > 0 && (/--/g).test(str)){
		str = str.replace(/--/g, '-');
	}
	return str.toLowerCase();
};
var data_search_sugesstion = document.getElementsByClassName("list");
var data_search_sugesstion = jQuery.makeArray(data_search_sugesstion);
data_search_sugesstion.reverse();
data_search_sugesstion = data_search_sugesstion.map(data => data.innerHTML); //đây là dữ liệu lấy về dưới dạng mảng
const handleSource = ({ term }, response) => {  //biến term này do jquery định nghĩa, là biến lấy dữ liệu khi nhập input search
    response(data_search_sugesstion.filter(item => {
        const comparedWith = KhongDau(item); //chuyển dữ liệu trong mảng lấy được thành chữ không dấu
        const query = KhongDau(term); //chuyển dữ liệu nhập trong input search về không dấu lun
        return comparedWith.indexOf(query) !== -1; // so sánh 2 biến comparedWith và query xem có khớp nhau ko, khớp mới đc return về
    }))
}

$("#search-input").autocomplete({ /* sử dụng jquery autocomplete để tạo chức năng search sugesstion */
    autoFocus: true,
    source:  handleSource //đưa dữ liệu đã được xử lý bên trên vào
}).keydown(function(event){
    if(event.keyCode == 13) {
      if($("#search-input").val().length==0) {+
          event.preventDefault();
          return false;

      }
       $("#submit").click();  /*tự động click button khi chọn option ở ô search*/
       console.log("đã nhấn enter")

    }
 });

 $( "#search-input" ).autocomplete(   /* xử lý sự kiện khi nhấn vào từng mục gợi ý của search thì mới chạy*/
    {
         source: handleSource,
         select: function(event, ui) {
            $("#search-input").val(ui.item.value);
            $("#submit").click();
  }
    })
/*Kết thúc Xử lý Chức năng Search Suggestion  */


/* -------------chức năng chuyển background color của item menu khi click vào*/
 var pathname = window.location.pathname;
         atag = $('.nav-item  a[href="'+pathname+'"]  ');
         atag.parent().addClass("activeMenu");
/* -------End------chức năng chuyển background color của item menu khi click vào*/

/* ---------Chức năng ẩn hiện comment và phản hồi khi nhấn nút phản hồi -----------*/
$('.comment-reply-btn').click(function(event){
   event.preventDefault();
   $(this).parent().next(".Reply_Comment").fadeToggle();

})
/* -----End----Chức năng ẩn hiện comment và phản hồi khi nhấn nút phản hồi -----------*/


});




