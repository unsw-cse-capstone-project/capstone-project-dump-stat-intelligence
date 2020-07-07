import styles from "./Modal.module.scss";

import { useDispatch } from "react-redux";

export default function Login(props) {
  const dispatch = useDispatch();
  function toggle() {
    document.getElementById(props.id).classList.toggle("is-active");
    if (props.func) {
      dispatch(props.func());
    }
  }
  return (
    <div id={props.id} className="modal">
      <div className="modal-background" onClick={toggle} />
      <div className={`modal-content ${styles.box}`}>{props.content}</div>
      <button
        className="modal-close is-large"
        aria-label="close"
        onClick={toggle}
      ></button>
    </div>
  );
}
