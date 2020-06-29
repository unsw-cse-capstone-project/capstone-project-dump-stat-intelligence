import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";
import { useDispatch } from 'react-redux';
import { login } from "../../lib/redux/actions/authAction";

export default function Login(props) {
    const dispatch = useDispatch();
    const alertName = props.login + "-alert"
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    function inn(event) {
        event.preventDefault();
        dispatch(login(event.target.elements.email.value, event.target.elements.password.value));
        
        event.target.elements.email.value = "";
        event.target.elements.password.value = "";
        //ONLY IF LOGIN SUCCEEDED, CLOSE MODAL AND EMPTY VALS
        if (true) {
            document.getElementById(alertName).innerHTML = "";
            document.getElementById(alertName).classList.remove(styles.show);
            toggle(props.login);
            
        } else {
            document.getElementById(alertName).innerHTML = "Incorrect login details. Please try again."
            document.getElementById(alertName).classList.add(styles.show);
            //NEED TO DISPLAY ERROR MESSAGE HERE
        }        
    }
    let content = <form onSubmit={inn}>
        <div className="form">
            <h3 className="title is-3">Sign in</h3>
            <div id={alertName} className={`${styles.alert} notification is-primary`}>
                
            </div>
            <hr/>
            <label className="label">Email</label>
            <div className="field control">
                <input name="email" className="input" type="text" placeholder="Email"/>
            </div>
            <label className="label">Password</label>
            <div className="field control">
                <input name="password" className="input" type="password" placeholder="Password"/>
            </div>
            <hr/>
            <div className="field control">
                <button type="submit" className="button is-link">Sign in</button>
            </div>
            <hr/>
            <p>Don't have an account? <span onClick={() => {toggle(props.login); toggle(props.register)}} className={styles.register}>Register</span></p>
        </div>
    </form>
    return <Modal id={props.login} content={content}/>
}