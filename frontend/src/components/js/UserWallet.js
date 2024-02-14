import { Button, Modal, Table, Tag } from 'antd';
import React, { useCallback, useContext, useEffect, useRef, useState } from 'react';
import { Link, useParams } from "react-router-dom";
import { AuthContext } from '../../context/AuthContext';
import useAxios from "../../utils/useAxios";
import '../component.css';



export default function UserWallet(){
    const { user_id } = useParams();
    const api = useRef(useAxios())
    const {messageApi} = useContext(AuthContext)
    const [walletDetails, setWalletDetails] = useState(null);
    const [transactions, setTransactions] = useState(null)
    const [openManage, setOpenManage] = useState(false)


    const getUserWallet = useCallback(async() =>{
        await api.current.post('/qr_admin/user_wallet/',{"id":user_id})
            .then((res)=>{
                if(res.data.status === 1){
                    setWalletDetails(res.data.data[0])
                    setTransactions(res.data.data[0].transaction)
                }else{
                    messageApi.open({type: 'error',content: res.data.message})
                }
            })
            .catch((error)=>{
                messageApi.open({type: 'error',content: error.message})
            })

    },[user_id,messageApi])

    useEffect(()=>{
        getUserWallet()
    },[getUserWallet])

    const tran_columns = [
        {title:"Transaction On",dataIndex:"tran_on", width: '15%'},
        {title:"Description",dataIndex:"description", width: '30%'},
        {
            title:"Credit (₹)",
            dataIndex:"amount",
            width: '10%',
            render:(text,record, index)=>
                <>
                {record.tran_type === "credit"?
                    <p>{text} <i className='fa fa-arrow-down' style={{ color:'green', WebkitTransform: 'rotate(45deg)'}}></i></p>:
                    <p></p>
                }
                </>

        },
        {
            title:"Debit (₹)",
            dataIndex:"amount",
            width: '10%',
            render:(text,record, index)=>
            <>
            {record.tran_type === "debit"?
                <p>{text} <i className='fa fa-arrow-up' style={{ color:'red', WebkitTransform: 'rotate(45deg)'}}></i></p>:
                <p></p>
            }
            </>
        },
        {title:"Balance (₹)",dataIndex:"total_amount", render:(text)=><b>{text}</b>},
        {
            title:"Credit/Debit (Point)",
            dataIndex:"point",
            width: '15%',
            render:(text,record)=>
                <>
                    {record.tran_type === "debit"?
                        <Tag color={'red'}>{record.point}</Tag> :
                        <Tag color={'green'}>{text}</Tag>
                    }
                </>
        },
        {
            title:"Balance (Point)",
            dataIndex:"total_point",
            width: '10%',
            render:(text,record)=><b>{text}</b>
        }
    ]

    const handleOnSave =()=>{
        console.log("On save function calll")
    }
    return (
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>User Wallet</div>
            <div className="title_tab_div">
               <Link to="/user"><Button type="primary">Back to users</Button></Link>
               <Button type="primary" onClick={()=> setOpenManage(true)}>Manage Account</Button>
            </div>
        </div>
        <div className='main_tab'>
            {walletDetails && (
                <div className='wallet_div'>
                    <div>
                        <div>
                            <h2 style={{margin: '15px 0px -10px 0px'}}>{walletDetails.user__full_name}</h2>
                            <p>Mo: {walletDetails.user__mobile}</p>
                        </div>
                        <div>
                            <h1>&#8377; {walletDetails.balance}</h1>
                        </div>
                    </div>
                    <div>
                        <p>Points: {walletDetails.point}</p>
                        <p>Withdraw Balance: {walletDetails.withdraw_balance}</p>
                        <p>Withdraw Points: {walletDetails.withdraw_point}</p>
                    </div>
                </div>
            )}
            <h2>Transaction History</h2>
            {transactions && (
            <Table columns={tran_columns}
                dataSource={transactions} rowKey="id"
                size="small"
                scroll={{y: 400}}
            />
            )}
            <Modal
                title="Manage Account"
                open={openManage}
                onOk={handleOnSave}
                okText="Save"
                onCancel={()=>setOpenManage(false)}
            >
                <h3>Deactivate</h3>
                <div className='manage_checkbox'>
                    <label><input type='checkbox' />Account</label>
                    <label><input type='checkbox' />Wallet</label>
                    <label><input type='checkbox' />Credit Transaction</label>
                    <label><input type='checkbox' />Debit Transaction</label>
                </div><br></br>
                <div>
                    <textarea placeholder='Reason of deactivate' style={{ width: '450px', height: '80px'}}></textarea>
                </div>
            </Modal>
        </div>
    </>
    )

}