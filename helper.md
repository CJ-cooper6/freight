source venv/Scripts/activate
pyenv activate freight

pip freeze > requirement.txt
pip install -r requirements.txt



id

name	//品名

piece	//件数

cube   //立方

weight  //重量

imprest	//垫付款

package_number	//包装数

room	//房间

create_at

update_at


不使用蓝图的情况下需要在 create_app 函数内部导入定义好的路由

