import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";
import { register, clear_next } from "../../lib/redux/actions/authAction";
import { get_pantry } from "../../lib/redux/actions/pantryAction";
import { useDispatch, useSelector } from "react-redux";
import { useRouter } from "next/router";

export default function Register(props) {
  const dispatch = useDispatch();
  const router = useRouter();
  const next = useSelector((state) => state.auth.nextPage);
  const alertName = props.register + "-alert";
  function toggle(id, clas) {
    document.getElementById(id).classList.toggle(clas);
  }
  function close(id, clas) {
    toggle(id, clas);
    dispatch(clear_next());
  }
  function join(event) {
    event.preventDefault();
    dispatch(
      register(
        event.target.elements.username.value,
        event.target.elements.email.value,
        event.target.elements.password.value
      )
    ).then((res) => {
      if (res) {
        document.getElementById(alertName).innerHTML = "";
        document.getElementById(alertName).classList.remove(styles.show);
        // close(props.register);
        //LOGIN SUCCEEDED, GET PANTRY
        dispatch(get_pantry());
        if (next) {
          router.push(next);
          dispatch(clear_next());
        }
        toggle("auth-register", "is-active");
        router.push("/pantrypirate/explore");
      } else {
        document.getElementById(alertName).innerHTML =
          "Failed to register. Please make sure you are not already registered and the email is valid.";
        document.getElementById(alertName).classList.add(styles.show);
      }
    });
    //Either way, should reset form
    event.target.elements.username.value = "";
    event.target.elements.email.value = "";
    event.target.elements.password.value = "";
  }
  let content = (
    <>
      <form onSubmit={join}>
        <div className="form">
          <h3 className="title is-3">Make an account</h3>
          <div
            id={alertName}
            className={`${styles.alert} notification is-primary`}
          >
            There was an error trying to register this account. Please ensure
            your email is not already registered.
          </div>
          <hr />
          <label className="label">Username</label>
          <div className="field control">
            <input
              name="username"
              required={true}
              className="input"
              type="text"
              placeholder="Your swanky username"
            ></input>
          </div>
          <label className="label">Email</label>
          <div className="field control">
            <input
              name="email"
              required={true}
              className="input"
              type="email"
              placeholder="Email"
            ></input>
          </div>
          <label className="label">Password</label>
          <div className="field control">
            <input
              name="password"
              required={true}
              className="input"
              type="password"
              placeholder="Password"
            ></input>
          </div>
          <hr />
          <div className="field control">
            <button className="button is-link">Register</button>
          </div>
        </div>
      </form>
      <hr />
      <p>
        Already have an account?{" "}
        <span
          onClick={() => {
            toggle(props.register, "is-active");
            toggle(props.login, "is-active");
          }}
          className={styles.register}
        >
          Sign in
        </span>
      </p>
    </>
  );
  return <Modal id={props.register} content={content} func={clear_next} />;
}
