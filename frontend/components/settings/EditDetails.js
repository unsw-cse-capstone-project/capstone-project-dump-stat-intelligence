import styles from "./EditDetails.module.scss";

import Modal from "../modal/Modal";
import { useDispatch, useSelector } from "react-redux";
import { update_details } from "../../lib/redux/actions/authAction";

export default function EditDetails(props) {
  let deets = useSelector((state) => state.auth.userInfo);
  const dispatch = useDispatch();
  const alertName = props.login + "-alert";
  function toggle(id, clas) {
    document.getElementById(id).classList.toggle(clas);
  }
  function update(event) {
    event.preventDefault();
    dispatch(
      update_details(
        event.target.elements.username.value,
        event.target.elements.email.value,
        event.target.elements.password.value
      )
    );
    //Either way, should reset form
    //If succeeded, login and close
    if (true) {
      document.getElementById(alertName).classList.remove(styles.show);
      toggle(props.id, "is-active");
    } else {
      //DISPLAY ERROR MESSAGE
      document.getElementById(alertName).innerHTML =
        "Couldn't update. Please ensure all fields are filled out.";
      document.getElementById(alertName).classList.add(styles.show);
    }
  }

  let form = (
    <form onSubmit={update}>
      <div className="form">
        <h3 className="title is-3">Update details</h3>
        <div
          id={alertName}
          className={`${styles.alert} notification is-primary`}
        ></div>
        <hr />
        <label className="label">Username</label>
        <div className="field control">
          <input
            name="username"
            className="input"
            type="text"
            placeholder="Your Username"
            defaultValue={deets.username}
          ></input>
        </div>
        <label className="label">Email</label>
        <div className="field control">
          <input
            name="email"
            className="input"
            type="text"
            placeholder="Your Email"
            defaultValue={deets.email}
          ></input>
        </div>
        <label className="label">Old Password</label>
        <div className="field control">
          <input
            name="password"
            className="input"
            type="password"
            placeholder="Your Password"
            defaultValue={deets.old_password}
          ></input>
        </div>
        <hr />
        <div className="field control">
          <button className="button is-link">Update</button>
        </div>
      </div>
    </form>
  );
  return <Modal id={props.id} content={form} />;
}
