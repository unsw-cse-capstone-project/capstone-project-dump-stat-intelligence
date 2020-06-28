import style from "./Details.module.scss"

import EditPassword from "./EditPassword"

export default function Details(props) {

    return <div className={style.currDeets}>
        <h4 className="title is-4">Password</h4>
        <hr/>
        <button className="button" onClick={() => {document.getElementById("edit-pwd").classList.toggle("is-active")}}>Change Password</button>
        <EditPassword id="edit-pwd"/>
    </div>
}