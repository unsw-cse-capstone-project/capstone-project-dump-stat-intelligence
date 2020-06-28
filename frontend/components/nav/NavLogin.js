import styles from "./NavItem.module.scss";


export default function Login(props) {
    function toggleModal() {
        //TOGGLE DIFFERENT MODALS BASED ON LOGIN STATUS
        document.getElementById("auth-login").classList.toggle("is-active");
    }
    
    return <li className={styles.box} onClick={toggleModal}>
            {props.icon}
            <span className={styles.tag}>{props.name}</span>
        </li>
}