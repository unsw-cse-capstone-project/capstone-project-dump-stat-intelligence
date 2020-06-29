import styles from "./EditDetails.module.scss";
import Modal from "../modal/Modal"

import { useDispatch } from 'react-redux';
import { update_password } from "../../lib/redux/actions/authAction"

export default function(props) {
    const dispatch = useDispatch();
    const alertName = props.id + "-alert";
    function change(event) {
        event.preventDefault();
        dispatch(update_password(event.target.elements.old.value, event.target.elements.pwd.value));
        //Reset form
        event.target.elements.old.value = null;
        event.target.elements.pwd.value = null;

        if (true) {
            document.getElementById(alertName).innerHTML = "";
            document.getElementById(alertName).classList.remove(styles.show);
            document.getElementById(props.id).classList.toggle("is-active");
            
        } else {
            document.getElementById(alertName).innerHTML = "Incorrect old password. Please try again."
            document.getElementById(alertName).classList.add(styles.show);
            //NEED TO DISPLAY ERROR MESSAGE HERE
        }   

    }
    let form = <form onSubmit={change}>
        <h3 className="title is-3">Change password</h3>
        <div id={alertName} className={`${styles.alert} notification is-primary`}>
                
        </div>
        <hr/>
        <label className="label">Old password</label>
        <div className="field control">
            <input required={true} name="old" className="input" type="password" placeholder="..."></input>
        </div>
        <label className="label">New password</label>
        <div className="field control">
            <input required={true} name="pwd" className="input" type="password" placeholder="..."></input>
        </div>
        <hr/>
        <div className="field control">
            <button type="submit" class="button is-link">Update</button>
        </div>
    </form>
    return <Modal id={props.id} content={form}/>
}