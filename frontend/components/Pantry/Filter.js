import styles from "./Filer.module.scss"

export default function Filter() {

    return <div className={styles.filterBox}>
        <form className={styles.filterForm}>
            <select className={styles.option}>
                <option>Breakfast</option>    
                <option>Lunch</option>    
                <option>Dinner</option>    
            </select>
            <select className={styles.option}>
                <option>Vegan</option>
                <option>Vegetarian</option>
                <option>Gluten Free</option>
                <option>Dairy Free</option>
            </select>

            <button className={`${styles.option} button is-button`}>Update</button>
        </form>


    </div>



}