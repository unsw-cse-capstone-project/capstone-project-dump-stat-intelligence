import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";
import { register } from "../../lib/redux/actions/authAction"
import { useDispatch } from 'react-redux';

export default function Register(props) {
    const dispatch = useDispatch();
    const alertName = props.register + "-alert"
    function toggle(id, clas) {
        document.getElementById(id).classList.toggle(clas);
    }
    function join(event) {
        event.preventDefault();
        dispatch(register(
            event.target.elements.first.value,
            event.target.elements.last.value,
            event.target.elements.email.value,
            event.target.elements.phone.value,
            event.target.elements.password.value
            ))
        //Either way, should reset form
        event.target.elements.first.value = ""
        event.target.elements.last.value = ""
        event.target.elements.email.value = ""
        event.target.elements.phone.value = ""
        event.target.elements.password.value = ""
        //If succeeded, login and close 
        if (true) {
            document.getElementById(alertName).classList.remove(styles.show);
            toggle(props.register, "is-active")
        } else {
            //DISPLAY ERROR MESSAGE
            document.getElementById(alertName).classList.add(styles.show);
        }
    }
    let content = <>
        <form onSubmit={join} >
            <div className="form">
                <h3 className="title is-3">Make an account</h3>
                <div id={alertName} className={`${styles.alert} notification is-primary`}>
                    There was an error trying to register this account. Please ensure your email is not already registered.
                </div>
                <hr/>
                <label className="label">Name</label>
                <div className="field-body field control">
                    <div className="field control">
                        <input name="first" required={true} className="input" type="text" placeholder="First Name"/>
                    </div>
                    <div className="field control">
                        <input name="last" required={true} className="input" type="text" placeholder="Last Name"/>
                    </div>
                </div>
                <label className="label">Email</label>
                <div className="field control">
                    <input name="email" required={true} className="input" type="email" placeholder="Email"></input>
                </div>
                <label className="label">Phone Number</label>
                <div className="field control">
                    <input name="phone" required={true} className="input" type="tel" placeholder="Your Phone Number"></input>
                </div>
                <label className="label">Password</label>
                <div className="field control">
                    <input name="password" required={true} className="input" type="password" placeholder="Password"></input>
                </div>
                <hr/>
                <div className="field control">
                    <button className="button is-link">Register</button>
                </div>
            </div>
        </form>
        <hr/>
        <p>Already have an account? <span onClick={() => {toggle(props.register, "is-active"); toggle(props.login, "is-active")}} className={styles.register}>Sign in</span></p>
    </>
    return <Modal id={props.register} content={content}/>


}