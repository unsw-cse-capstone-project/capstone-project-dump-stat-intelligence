import styles from "./EditDetails.module.scss";

import Modal from "../modal/Modal";
import { useDispatch, useSelector } from 'react-redux';
import { update_details } from "../../lib/redux/actions/authAction";

export default function EditDetails(props) {
    let deets = useSelector(state => state.auth.userInfo)
    const dispatch = useDispatch();
    const alertName = props.login + "-alert"
    function toggle(id, clas) {
        document.getElementById(id).classList.toggle(clas);
    } 
    function update(event) {
        event.preventDefault();
        dispatch(update_details(
            event.target.elements.first.value,
            event.target.elements.last.value,
            event.target.elements.email.value,
            event.target.elements.phone.value
            ))
        //Either way, should reset form
        //If succeeded, login and close 
        if (true) {
            document.getElementById(alertName).classList.remove(styles.show);
            toggle(props.id, "is-active")
        } else {
            //DISPLAY ERROR MESSAGE
            document.getElementById(alertName).innerHTML = "Couldn't update. Please ensure all fields are filled out."
            document.getElementById(alertName).classList.add(styles.show);
        }
    }
    
    let form = <form onSubmit={update}>
        <div className="form">
            <h3 className="title is-3">Update details</h3>
            <div id={alertName} className={`${styles.alert} notification is-primary`}>
                
            </div>
            <hr/>
            <label className="label">Name</label>
            <div className="field-body field control">
                <div className="field control">
                    <input name="first" className="input" type="text" placeholder="First Name" defaultValue={deets.first}/>
                </div>
                <div className="field control">
                    <input name="last" className="input" type="text" placeholder="Last Name" defaultValue={deets.last}/>
                </div>
            </div>
            <label className="label">Email</label>
            <div className="field control">
                <input name="email" className="input" type="text" placeholder="Your Address" defaultValue={deets.email}></input>
            </div>
            <label className="label">Phone Number</label>
            <div className="field control">
                <input name="phone" className="input" type="tel" placeholder="Your Phone Number" defaultValue={deets.phone}></input>
            </div>
            <hr/>
            <div className="field control">
                <button className="button is-link">Update</button>
            </div>
        </div>
    </form>
    return <Modal id={props.id} content={form}/>
}