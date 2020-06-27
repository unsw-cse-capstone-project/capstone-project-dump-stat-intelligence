import style from "./Details.module.scss"

import EditDetails from "./EditDetails" 

export default function Details(props) {
    let deets = [["Name", props.name],["Email Address", props.email],["Phone", props.phone],["Address", props.address]]
    
    return <div className={style.currDeets}>
        <h4 className="title is-4">Current details</h4>
        <hr/>
        {deets.map((item, idx) => <div key={idx}>
            <span className={style.category}>{item[0]}: </span> {item[1]} <br/>
        </div>)}
        <br/>
        <button className="button" onClick={() => {document.getElementById("edit-deets").classList.toggle("is-active")}}>Edit details</button>
        <EditDetails id="edit-deets"/>
        
    </div>
}