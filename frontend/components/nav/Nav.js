import styles from './Nav.module.scss'
import Brand from '../icons/Brand'
import Explore from '../icons/Explore'
import Cookbook from '../icons/Cookbook'
import Create from '../icons/Create'
import Settings from '../icons/Settings'
import Pantry from '../icons/Pantry'
import NavItem from './NavItem'

export default function Nav() {

    return <nav className={styles.nav}>

        <ul>
            <NavItem icon={<Brand/>} brand={true}/>
            <NavItem icon={<Explore/>} name={'Explore'}/>
            <NavItem icon={<Pantry/>} name={'Pantry'}/>
            <NavItem icon={<Cookbook/>} name={'Cookbook'}/>
            <NavItem icon={<Create/>} name={'Create'}/>
            <NavItem icon={<Settings/>} name={'Settings'}/>
        </ul>

    </nav>
        
    
}