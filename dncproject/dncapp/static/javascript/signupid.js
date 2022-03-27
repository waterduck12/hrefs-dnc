function id_overlap_check() {

    $('.username').change(function () {
      $('#id_check_sucess').hide();
      $('.id_overlap_button').show();
      $('.username').attr("check_result", "fail");
    })


    if ($('.username').val() == '') {
      alert('이메일을 입력해주세요.')
      return;
    }

    id_overlap_input = document.querySelector('input[name="username"]');

    $.ajax({
      url: "{% url account:id_overlap_check' %}",
      data: {
        'username': id_overlap_input.value
      },
      datatype: 'json',
      success: function (data) {
        console.log(data['overlap']);
        if (data['overlap'] == "fail") {
          alert("이미 존재하는 아이디 입니다.");
          id_overlap_input.focus();
          return;
        } else {
          alert("사용가능한 아이디 입니다.");
          $('.username').attr("check_result", "success");
          $('#id_check_sucess').show();
          $('.id_overlap_button').hide();
          return;
        }
      }
    });
  }

  if ($('.username').attr("check_result") == "fail"){
    alert("아이디 중복체크를 해주시기 바랍니다.");
    $('.username').focus();
    return false;
  }