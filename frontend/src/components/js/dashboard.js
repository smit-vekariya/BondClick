import { LogoutOutlined, UserOutlined } from '@ant-design/icons';
import { Dropdown, Flex, Layout, Menu, theme } from 'antd';
import 'font-awesome/css/font-awesome.min.css';
import React, { memo, useCallback, useContext, useEffect, useRef, useState } from 'react';
import { Link, Outlet } from "react-router-dom";
import { AuthContext } from '../../context/AuthContext';
import useAxios from '../../utils/useAxios';
import "../component.css";
import logo_char from './logo-char.png';
import logo from './logo-no-background.png';


const { Header, Content, Footer, Sider } = Layout;
function getItem(label, key, icon, children) {
  return {
    key,
    icon,
    children,
    label,
  };
}
const Dashboard = () => {
  const api = useRef(useAxios())
  const [collapsed, setCollapsed] = useState(false);
  const [menuData, setMenuData] = useState(()=>localStorage.getItem("main_menu") ? JSON.parse(localStorage.getItem("main_menu")):{});
  const {user,logoutUser} = useContext(AuthContext)

  // useEffect(() => {
  //   if(Object.keys(menuData).length === 0){
  //       getMainMenu()
  //     }
  // },[menuData])

  let getMainMenu = useCallback(async () =>{
      await api.current.get("/account/main_menu/")
        .then((res)=>{
          setMenuData(res["data"])
          localStorage.setItem("main_menu", JSON.stringify(res["data"]))
        })
  },[])

  useEffect(() => {
      getMainMenu()
  },[getMainMenu])


  var new_list = []
  var nested_list = []
  var parent = null
  for(let [key,v] of Object.entries(menuData)){
      let k = parseInt(key)
      if(menuData[k+1]){
        if ((v.sequence).split(".")[0] === ((menuData[k+1]).sequence).split(".")[0]){
          parent = parent === null ? k : parent
          nested_list.push(getItem(<Link to={menuData[k+1].url}>{menuData[k+1].name}</Link>, menuData[k+1].id,<i className={menuData[k+1].icon} />))
        }else{
          if(parent != null){
            new_list.push(getItem(menuData[parent].name, menuData[parent].id, <i className={menuData[parent].icon} /> ,nested_list))
            parent = null
            nested_list =[]
          }else{
            // below line is use full, remove temporary for bond click requirement and add new line that second from below line
            // new_list.push(getItem(v.name, v.id, <i className={v.icon} />))
            new_list.push(getItem(<Link to={v.url}>{v.name}</Link>, v.id, <i className={v.icon} />))
          }
        }
      }else{
        new_list.push(getItem(<Link to={v.url}>{v.name}</Link>, v.id, <i className={v.icon} />))
      }
  }

  let fixed_items = [getItem((<img src={logo} alt="logo-no-background.png" style={{width:"150px"}}></img>), '0', (collapsed ? <img src={logo_char} alt="logo-char.png" style={{width:"20px"}}></img>:""))]
  let menu_items =[...fixed_items,...new_list]

  const items = [
    getItem((<Link to="/profile">My Profile</Link>), '1', <UserOutlined />),
    // getItem((<Link to="/register">Register</Link>), '2', <UserAddOutlined />),
    getItem((<Link onClick={logoutUser}>Logout</Link>), '3', <LogoutOutlined />),
  ];


  const {
    token: { colorBgContainer },
  } = theme.useToken();


  return (
    <Layout style={{minHeight: '100vh'}}>
      <Sider collapsible collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
        <div className="demo-logo-vertical" />
        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={menu_items} />
      </Sider>
      <Layout>
        <Header style={{padding: 0, background: colorBgContainer}}>
            <Flex gap="small" wrap="wrap" style={{float: "right", marginRight:"10px"}}>
                <Dropdown.Button menu={{items}} style={{margin: "9px 0px 5px 1px"}} placement="bottomLeft" icon={<UserOutlined />}>{user && user.full_name}</Dropdown.Button>
            </Flex>
        </Header>
        <Content className='content_class'>
          <Outlet/>
        </Content>
        <Footer style={{textAlign: 'center'}}>
        </Footer>
      </Layout>
    </Layout>
  );
};
export default memo(Dashboard);



// Converting the array string to an actual array
// const menu_items = [
//   getItem((<img src={logo} alt="logo-no-background.png" style={{width:"150px"}}></img>), '0', (collapsed ? <img src={logo_char} alt="logo-char.png" style={{width:"20px"}}></img>:"")),
//   getItem('Admin', '1', <UserOutlined />, [
//     getItem((<Link to="/user">User</Link>), '1.1', <UserAddOutlined /> ),
//     getItem((<Link to="/permissions">Permissions</Link>), '1.2', <ReadOutlined />),
//   ]),
//   getItem((<Link to="/about_us">About Us</Link>), '2', <ProjectOutlined />),
// ];

