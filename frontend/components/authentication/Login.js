import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";
import { useDispatch, useSelector } from 'react-redux';
import { login, clear_next } from "../../lib/redux/actions/authAction";
import { create_pantry } from "../../lib/redux/actions/pantryAction";
import { useRouter } from "next/router";

export default function Login(props) {
    const dispatch = useDispatch();
    const router = useRouter();
    const next = useSelector(state => state.auth.nextPage);
    const alertName = props.login + "-alert"
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    function close(id) {
        toggle(id);
        dispatch(clear_next);
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
            close(props.login);
            //LOGIN SUCCEEDED, GET PANTRY
            dispatch(create_pantry());
            if (next) {
                router.push(next);
            }
            
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
                <input required={true} name="email" className="input" type="email" placeholder="Email"/>
            </div>
            <label className="label">Password</label>
            <div className="field control">
                <input required={true} name="password" className="input" type="password" placeholder="Password"/>
            </div>
            <hr/>
            <div className="field control">
                <button type="submit" className="button is-link">Sign in</button>
            </div>
            <hr/>
            <p>Don't have an account? <span onClick={() => {toggle(props.login); toggle(props.register)}} className={styles.register}>Register</span></p>
        </div>
    </form>
    return <Modal id={props.login} content={content} func={clear_next} />
}