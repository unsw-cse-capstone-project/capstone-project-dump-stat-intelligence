import styles from "./Modal.module.scss"


export default function Login(props) {
    function toggle() {
        document.getElementById(props.id).classList.toggle("is-active");
    }
    return <div id={props.id} className="modal">
        <div className="modal-background" onClick={toggle}/>
        <div className={`modal-content ${styles.box}`}>
            {props.content}

        </div>
        <button class="modal-close is-large" aria-label="close" onClick={toggle}></button>
    </div>

}