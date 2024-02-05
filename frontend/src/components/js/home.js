import React from "react";
import {Form, Button} from 'react-bootstrap';
import logo from './logo-no-background.png'
import { Link } from "react-router-dom";


export default function Home(){
    return(
    <>
        <div className="home_nav">
             <Link to="/login"><Button variant="outline-primary">Sign In</Button></Link>
             <Link to="/register"><Button variant="outline-warning">Sign Up</Button></Link>
        </div>
        <div className="main_div">
            <div className="login_div">
                <Form>
                    <Form.Group className="mb-3" controlId="formBasicEmail" style={{textAlign:'center'}}>
                        <img src={logo} alt="logo-no-background.png" style={{width:"400px"}}></img>
                    </Form.Group>
                </Form>
            </div>
            <div className="intro_div" style={{width: "60%"}}>
                <Form>
                    <Form.Group className="mb-3" controlId="formBasicEmail" style={{textAlign:'center'}}>
                        <p>Enterprise resource planning (ERP) refers to a type of software that organizations use to manage day-to-day business activities such as accounting, procurement, project management, risk management and compliance, and supply chain operations. A complete ERP suite also includes enterprise performance management, software that helps plan, budget, predict, and report on an organization’s financial results.ERP systems tie together a multitude of business processes and enable the flow of data between them. By collecting an organization’s shared transactional data from multiple sources, ERP systems eliminate data duplication and provide data integrity with a single source of truth.</p>
                        <p>Every business must complete work that requires numerous stakeholders with various responsibilities. But that’s a struggle when the information needed to execute processes and make key decisions is spread across disconnected systems. Whether data is held in basic business management software or spreadsheets, employees have a hard time finding what they need and may lack access to it entirely. For example, the accounting and FP&A teams could each have different spreadsheets with different figures for expense tracking.</p>
                        <p>These disparate data sources make it very challenging to keep everyone on the same page and hinders collaboration and efficiency, especially as an organization grows. Staff waste time hunting for documents and potentially duplicating work because there is no one place to look for up-to-date information on all aspects of the business relevant to them. This also makes it difficult to see the full cause and effect of developments affecting your business.</p>
                        <p>An ERP system solves this problem by compiling information in a central database to grant managers and employees cross-departmental visibility. It also eliminates the problems that come with conflicting sources of data and empowers them to analyze various scenarios, discover process improvements and generate major efficiency gains. That translates to cost savings and better productivity as people spend less time digging for needed data.</p>
                    </Form.Group>
                </Form>
            </div>
        </div>
    </>
    )
}