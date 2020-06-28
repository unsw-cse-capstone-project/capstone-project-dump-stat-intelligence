import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";

export default function Login(props) {
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    
    let content = <form>
        <div className="form">
            <h3 className="title is-3">Sign in</h3>
            <hr/>
            <label className="label">Username</label>
            <div className="field control">
                <input className="input" type="text" placeholder="Username"/>
            </div>
            <label className="label">Password</label>
            <div className="field control">
                <input className="input" type="password" placeholder="Password"/>
            </div>
            <hr/>
            <div className="field control">
                <button class="button is-link">Sign in</button>
            </div>
            <hr/>
            <p>Don't have an account? <span onClick={() => {toggle(props.login); toggle(props.register)}} className={styles.register}>Register</span></p>
        </div>
    </form>
    return <Modal id={props.login} content={content}/>
}