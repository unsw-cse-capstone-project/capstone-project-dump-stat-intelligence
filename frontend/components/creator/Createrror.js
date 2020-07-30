import styles from "./Edit.module.scss";

import Modal from "../modal/Modal";


export default function createrror() {
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    let content = <div className="form">
        <h3 className="title is-3">Hang on - you're not done!!</h3>
        <div className="field">
            You seem to have left some recipe fields empty. Please make sure they are all filled out!
        </div>
        <div className="field is-grouped">
            <div className="control">
                <button onClick={() => {toggle("createrror")}} className="button is-primary">Ok</button>
            </div>
        </div>
    </div>
    return <Modal id="createrror" content={content}/>
}