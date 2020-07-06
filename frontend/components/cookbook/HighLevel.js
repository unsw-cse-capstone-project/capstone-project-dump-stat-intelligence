import styles from "./HighLevel.module.scss";


export default function HighLevel() {

    return <div className={styles.box}>
        <div className={styles.thing}>
            <h1 className="title">points</h1>
            <p>Dropdown similar to pantry for :</p>
                <br/>
                <ul>
                    <li>&nbsp;&nbsp;&nbsp;mY FAVourited recipes</li>
                    <li>&nbsp;&nbsp;&nbsp;my own created recipes</li>
                    <li>&nbsp;&nbsp;&nbsp;is that all that is on this page???</li>
                </ul>
            <br/>
            <br/>
            <p>Need to have a new recipecard icon for these to have edit and unfavourite icons??</p>
            
        </div>
        <div className={styles.thing}>
            <h1 className="title">Dropdown - content shows all your favourited recipes</h1>
        </div>
        <div className={styles.thing}>
            <h1 className="title">Dropdown - content shows all your written recipes</h1>
        </div>

    </div>
}