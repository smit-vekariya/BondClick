import { Button, Input, Table } from "antd";
import React, { useCallback, useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import useAxios from "../../utils/useAxios";


export default function UsersWalletReport(){
    const api = useRef(useAxios())
    const { Search } = Input;
    const [walletData , setWalletData] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const {messageApi} = useContext(AuthContext)
    const [filterDict, setFilterDict] =useState({page:1,pageSize:10,orderBy:"-balance",search:""})

    const getUsersWalletData = useCallback(async() =>{
        await api.current.get(`/qr_admin/users_wallet_report/?page=${filterDict.page}&page_size=${filterDict.pageSize}&ordering=${filterDict.orderBy}&search=${filterDict.search}`)
        .then((res)=>{
            setTotalRecord(res.data.count)
            setWalletData(res.data.results)
        })
        .catch((error)=>{
            messageApi.open({type: 'error', content:error.message})
        })

    },[filterDict, messageApi])

    useEffect(()=>{
        getUsersWalletData()
    },[getUsersWalletData])

    const columns = [
        {title:"User", dataIndex:"user__mobile", sorter: true},
        {title:"Balance (₹)", dataIndex:"balance", sorter: true},
        {title:"Withdraw Balance (₹)", dataIndex:"withdraw_balance", sorter: true},
        {title:"Point", dataIndex:"point", sorter: true},
        {title:"Withdraw Point", dataIndex:"withdraw_point", sorter: true}
    ]

    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }

    const onTableChange = (pagination, filters, sorter) =>{
        var orderBy = sorter.order ? (sorter.order === "ascend"? "":"-") + sorter.field : "-id"
        setFilterDict({...filterDict,page:pagination.current,pageSize:pagination.pageSize,orderBy:orderBy})
    }
    return(
        <>
            <div className='title_tab'>
                <div className='title_tab_title'>Users Wallet Report</div>
                <div className="title_tab_div">
                    <Search placeholder="Search by user" allowClear={true} onChange={(e)=> {if(e.target.value===""){setFilterDict({...filterDict, search:""})}}} onSearch={(value) => setFilterDict({...filterDict, search:value})} style={{ width: 200 }} />
                </div>
            </div>
            <div className='report_tab'>
                <div>
                    <label>Top <input type="number" min={0} placeholder="" />
                        <select name="balance" id="balance">
                            <option value="highest_balance">Highest Balance</option>
                            <option value="highest_withdraw">Highest Withdraw</option>
                        </select>
                    </label>
                   <Button type="primary">Load</Button>
                   <Button>Reset</Button>
                </div>
                <div>
                   <Button type="primary">Export</Button>
                </div>
            </div>
            <div className='main_tab'>
                <Table
                    columns={columns}
                    dataSource={walletData} rowKey="id"
                    onChange={onTableChange}
                    rowSelection={{selectedRowKeys,onChange: onSelectChange}}
                    pagination={{total: totalRecord,
                        defaultPageSize: 10, showSizeChanger: true,
                        pageSizeOptions: ['10', '20', '50', '100'],
                    }}
                    footer={() => ( <div style={{textAlign:'right'}}>Selected Records ({selectedRowKeys.length} of {totalRecord})</div>)}
                    scroll={{y: 500}}
                    size="small"/>
            </div>
        </>
    )

}