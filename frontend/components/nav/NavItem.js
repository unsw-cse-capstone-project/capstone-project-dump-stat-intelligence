import styles from './NavItem.module.scss'

export default function NavItem(props) {
    return <li className={'brand' in props ? styles.brand : styles.box}>
        {props.icon}
        {'brand' in props ? '' : 
        <span className={styles.tag}>
            {props.name}
        </span>
        }
        
    </li>
}