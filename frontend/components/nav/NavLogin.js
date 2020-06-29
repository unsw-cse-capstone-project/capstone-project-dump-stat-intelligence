import styles from "./NavItem.module.scss";


export default function Login(props) {
    function toggleAuth() {
        
        if (props.isLoggedIn) {
            document.getElementById(props.logout).classList.toggle("is-active");
        } else {
            document.getElementById(props.login + "-alert").innerHTML = "";
            document.getElementById(props.login + "-alert").classList.remove(styles.show);
            document.getElementById(props.login).classList.toggle("is-active");
        }
    }
    
    return <li className={styles.box} onClick={toggleAuth}>
            {props.icon}
            <span className={styles.tag}>{props.isLoggedIn ? "Sign out" : "Sign in / Register"}</span>
        </li>
}