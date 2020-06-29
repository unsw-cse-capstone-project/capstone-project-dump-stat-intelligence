import style from "./Details.module.scss"

import EditDetails from "./EditDetails" 
import { useSelector } from 'react-redux';

export default function Details(props) {
    let deets = useSelector(state => state.auth.userInfo)
    
    
    return <div className={style.currDeets}>
        <h4 className="title is-4">Current details</h4>
        <hr/>
        <span className={style.category}>Name: </span> {deets.first} {deets.last} <br/>
        <span className={style.category}>Email: </span> {deets.email} <br/>
        <span className={style.category}>Phone: </span> {deets.phone} <br/>
        <br/>
        <button className="button" onClick={() => {document.getElementById("edit-deets").classList.toggle("is-active")}}>Edit details</button>
        <EditDetails id="edit-deets"/>
        
    </div>
}