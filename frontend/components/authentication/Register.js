import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";



export default function Register(props) {
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    let content = <>
        <form>
            <div className="form">
                <h3 className="title is-3">Make an account</h3>
                <hr/>
                <label className="label">Name</label>
                <div className="field-body field control">
                    <div className="field control">
                        <input class="input" type="text" placeholder="First Name"/>
                    </div>
                    <div className="field control">
                        <input class="input" type="text" placeholder="Last Name"/>
                    </div>
                </div>
                <label className="label">Phone Number</label>
                <div className="field control">
                    <input className="input" type="tel" placeholder="Your Phone Number"></input>
                </div>
                <label className="label">Address</label>
                <div className="field control">
                    <input className="input" type="text" placeholder="Your Address"></input>
                </div>
                <label className="label">Password</label>
                <div className="field control">
                    <input className="input" type="password" placeholder="Password"></input>
                </div>
                <hr/>
                <div className="field control">
                    <button class="button is-link">Register</button>
                </div>
            </div>
        </form>
        <hr/>
        <p>Already have an account? <span onClick={() => {toggle(props.register); toggle(props.login)}} className={styles.register}>Sign in</span></p>
    </>
    return <Modal id={props.register} content={content}/>


}