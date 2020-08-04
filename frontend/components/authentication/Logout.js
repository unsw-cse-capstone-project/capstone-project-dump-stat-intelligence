import styles from "./Auth.module.scss";

import Modal from "../modal/Modal";
import { useDispatch } from 'react-redux';
import { logout } from "../../lib/redux/actions/authAction";
import Router from 'next/router';


export default function Logout(props) {
    const dispatch = useDispatch();
    function toggle(id) {
        document.getElementById(id).classList.toggle("is-active");
    }
    function out() {
        toggle(props.logout);
        dispatch(logout());
        Router.push('/pantrypirate');
    }
    let content = <div className="form">
        <h3 className="title is-3">Are you sure you want to sign out?</h3>
        <hr/>
        <div className="field is-grouped">
            <div className="control">
                <button onClick={out} className="button is-link">Sign out</button>
            </div>
            <div className="control">
                <button onClick={() => {toggle(props.logout)}} className="button">Cancel</button>
            </div>
        </div>
    </div>
    return <Modal id={props.logout} content={content}/>


}