import { Button, Modal, Table } from 'antd';
import React, { useCallback, useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from '../../context/AuthContext';
import useAxios from "../../utils/useAxios";
import '../component.css';

export default function User(){
    const api = useRef(useAxios())
    const [users, setUsers] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const [isWalletOpen, setIsWalletOpen] =useState(false)
    const {messageApi} = useContext(AuthContext)
    const [page, setPage] = useState(1);
    const [pageSize, setPageSize] = useState(10);
    const [orderBy, setOrderBy] = useState("-id");
    const [walletDetails, setWalletDetails] = useState([]);


    let getUserData = useCallback(async () =>{
        await api.current.get(`/qr_admin/user_list/?page=${page}&page_size=${pageSize}&ordering=${orderBy}`,
            // {
            //     params:{"full_name":"tester"}
            // }
            )
            .then((res)=>{
                setTotalRecord(res.data.count)
                setUsers(res.data.results)
            })
            .catch((error)=>{
                messageApi.open({type: 'error',content: error.message})
            })
    },[page, pageSize, orderBy,messageApi])

    useEffect(()=>{
        getUserData();
    }, [getUserData])


    const columns = [
        {title:"Name",dataIndex:"full_name",sorter: true},
        {title:"Mobile No.",dataIndex:"mobile",sorter: true},
        {title:"Address",dataIndex:"address",sorter: true},
        {title:"Pin Code",dataIndex:"pin_code",sorter: true},
        {title:"City",dataIndex:"city__name", sorter: true},
        {title:"State",dataIndex:"state__name",sorter: true},
        {title:"Distributor",dataIndex:"distributor__name",sorter: true},
    ]

    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }

    const onTableChange = (pagination, filters, sorter) =>{
        setPage(pagination.current);
        setPageSize(pagination.pageSize)
        var order_by = sorter.order ? (sorter.order === "ascend"? "":"-") + sorter.field : "-id"
        setOrderBy(order_by)
    }

    const viewWallet = async() =>{
        if(selectedRowKeys.length !== 1){
            messageApi.open({type: 'error',content: "Please select one user."});
            return
        }
        await api.current.post('/qr_admin/user_wallet/',{"id":selectedRowKeys[0]})
            .then((res)=>{
                if(res.data.status === 1){
                    console.log(res.data.data[0])
                    setWalletDetails(res.data.data)
                    setIsWalletOpen(true)
                }else{
                    messageApi.open({type: 'error',content: res.data.message})
                }
            })
            .catch((error)=>{
                messageApi.open({type: 'error',content: error.message})
            })

    }

    return(
    <>
       <div className='title_tab'>
            <div className='title_tab_title'>Bond Users</div>
            <div className="title_tab_div">
               <Button type="primary" onClick={viewWallet}>View Wallet</Button>
            </div>
        </div>
        <div className='main_tab'>
        <Table
            columns={columns}
            dataSource={users} rowKey="id"
            onChange={onTableChange}
            rowSelection={{selectedRowKeys,onChange: onSelectChange}}
            pagination={{total: totalRecord,
                defaultPageSize: 10, showSizeChanger: true,
                pageSizeOptions: ['10', '20', '50', '100'],
            }}
            scroll={{y: 500}}
            size="small"/>
        </div>
        <Modal title="User Wallet" width={1200} open={isWalletOpen} okText="Ok" onOk={()=>setIsWalletOpen(false)} onCancel={()=>setIsWalletOpen(false)}>
                {walletDetails.map(data =>
                <div key={data.id}>
                    <p>Full Name: {data.user__full_name}</p>
                    <p>Mobile Number: {data.user__mobile}</p>
                    <p>Balance: {data.balance}</p>
                    <p>Points: {data.point}</p>
                    <p>Withdraw Balance: {data.withdraw_balance}</p>
                    <p>Withdraw Points: {data.withdraw_point}</p>
                    <h2>Transaction:</h2>
                    {(data.transaction).map((tran, index) => <div key={index}>
                        <p>Description: {tran.description}</p>
                        <p>amount: {tran.amount}</p>
                        <p>point: {tran.point}</p>
                        <p>total_point: {tran.total_point}</p>
                        <p>total_amount: {tran.total_amount}</p>
                        <p>tran_on: {tran.tran_on}</p>
                        <p>tran_type: {tran.tran_type}</p>
                    </div>)}
                </div>
                )}

        </Modal>
    </>
    )
}
