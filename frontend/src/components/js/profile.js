import { Form, Input } from 'antd';
import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import useAxios from "../../utils/useAxios";
import '../component.css';

export default function Profile(){
    const api = useAxios()
    const [profile, setProfile] = useState({})
    const {messageApi} = useContext(AuthContext)

    useEffect(()=>{
        getProfileData()
    },[])

    const getProfileData = async() =>{
        await api.get('/account/user_profile/')
        .then((res)=>{
            if(res.data.status === 1){
                setProfile(res.data.data[0][0])
                console.log("res.data.data", res.data.data[0][0]);
            }
            else{
                messageApi.open({type: 'error',content: res.data.message})
            }
        })
    }


    return (
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>Profile</div>
        </div>
        <div className='main_tab'>
            <Form  style={{ maxWidth: 600,margin: '19px 6px'}}  labelCol={{flex: '110px'}} labelAlign="left">
                <Form.Item label="Full Name">
                    <Input type='text' value={profile.full_name} readOnly></Input>
                </Form.Item>
                <Form.Item label="Mobile No.">
                    <Input type='text' value={profile.mobile} readOnly></Input>
                </Form.Item>
                <Form.Item label="Address">
                    <Input type='text' value={profile.address} readOnly></Input>
                </Form.Item>
                <Form.Item label="Pin Code">
                    <Input type='text' value={profile.pin_code} readOnly></Input>
                </Form.Item>
                <Form.Item label="City">
                    <Input type='text' value={profile.city} readOnly></Input>
                </Form.Item>
                <Form.Item label="State">
                    <Input type='text' value={profile.state} readOnly></Input>
                </Form.Item>
            </Form>
        </div>
        </>
    )
}