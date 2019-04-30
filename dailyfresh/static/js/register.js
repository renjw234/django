$(function(){
	var error_name = false;
	var error_pwd = false;
	var error_cpwd = false;
	var error_email = false;
	var error_allow = false;

	$('#user_name').blur(function(){
		check_username();
	})
	$('#user_name').focus(function(){
		$(this).next().hide();
	})
	$('#pwd').blur(function(){
		check_pwd();
	})
	$('#pwd').focus(function(){
		$(this).next().hide();
	})
	$('#cpwd').blur(function(){
		check_cpwd();
	})
	$('#cpwd').focus(function(){
		$(this).next().hide();
	})
	$('#email').blur(function(){
		check_email();
	})
	$('#email').focus(function(){
		$(this).next().hide();
	})
	$('#allow').click(function(){
		if($(this).prop('checked')==true)
		{
			error_allow = false;
			$('.error_tip2').hide();
		}
		else
		{
			error_allow =true;
			$('.error_tip2').html('请勾选同意！').show();
		}
	})
	

	function check_username(){
/*		var val = $('#user_name').val();
		var re = /^\w{5,15}$/i;
		var a =1;
		if(val=='')
		{
			$('#user_name').next().html('用户名不能为空！').show();
			error_name = true;
			return;

		}
		if(re.test(val))
		{
			error_name = false;
		}

		if(a==1) {
			// $('#user_name').next().html('aaa！').show();
			$.get('/user/register_exist/?uname=' + $('#user_name').val(), function (data) {
				if (data.count == 1) {
					$('#user_name').next().html('222！').show();
					$('#user_name').next().html('用户已经存在').show();
					error_name = true;
				} else {
					$('#user_name').next().html('222！').show();
					$('#user_name').next().hide();
					error_name = false;
				}

			});
		}
		else
		{
			error_name = true;
			$('#user_name').next().html('用户名是5到15位的数字、字母、和下划线的格式！').show();
			error_name = true;
		}
	}*/
		var len=$('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名').show();
			error_name = true;
		}
		else
		{
			// $('#user_name').next().html('111').show();
			// $('#user_name').next().hide()
			// error_name=false;
			// alert('准备发送数据')
			$.get('/user/register_exist/?uname='+$('#user_name').val(),function (data) {

				// alert('开始判断count')
				// alert(data)
				if(data.count!=0){
					// alert(data.count)
					$('#user_name').next().html('用户名已经存在').show();
					error_name = true;
				}
				else {
					$('#user_name').next().hide();
					error_name=false;
				}
			})
			// alert('检测完毕')
		}
	}


	function check_pwd(){
		var val = $('#pwd').val();
		var re = /^[a-zA-Z0-9@\$\*\.\!\?]{6,16}$/;
		if(val=='')
		{
			$('#pwd').next().html('密码不能为空！').show();
			error_pwd = true;
			return;

		}
		if(re.test(val))
		{
			error_pwd = false;
		}
		else
		{
			error_pwd = true;
			$('#pwd').next().html('密码是6-16位的字母、数字和$@*。！？的格式！').show();
			error_pwd = true;
		}
	}

	function check_cpwd(){
		if($('#cpwd').val()=='')
		{
			$('#cpwd').next().html('密码不能为空！').show();
			error_pwd = true;
			return;
		}

		if($('#cpwd').val()==$('#pwd').val())
		{
			error_cpwd = false;
		}
		else
		{
			error_cpwd = true;
			$('#cpwd').next().html('您输入的密码不一致！请重新输入！').show();
		}
	}

	function check_email(){
		var val = $('#email').val();
		// var re = /^[a-zA-Z0-9][\w\.]*@[\w](\.[\w]{2,3}){2,3}$/;
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
		if(val=='')
		{
			$('#email').next().html('邮箱不能为空！').show();
			error_pwd = true;
			return;

		}
		if(re.test(val))
		{
			error_pwd = false;
		}
		else
		{
			error_pwd = true;
			$('#email').next().html('请输入正确的邮箱！').show();
			error_pwd = true;
		}
	}

	$('.reg_form').submit(function(){
		check_username();
		check_pwd();
		check_cpwd();
		check_email();

		if(!(error_name == false && error_pwd == false && error_cpwd == false
			&& error_email == false && error_allow == false)){
			return false;
		}		
	})

})