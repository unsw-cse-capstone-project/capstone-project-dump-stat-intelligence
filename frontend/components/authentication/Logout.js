import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";



export default function Logout(props) {
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    let content = <div className="form">
        <h3 className="title is-3">Are you sure you want to sign out?</h3>
        <hr/>
        <div class="field is-grouped">
            <div class="control">
                <button class="button is-link">Sign out</button>
            </div>
            <div class="control">
                <button onClick={() => {toggle(props.logout)}} class="button">Cancel</button>
            </div>
        </div>
    </div>
    return <Modal id={props.logout} content={content}/>


}