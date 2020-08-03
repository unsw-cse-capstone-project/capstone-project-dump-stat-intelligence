import styles from "./RecipeCard.module.scss";

import { useState } from 'react';

export default function Indication(props) {
    const [active, setActive] = useState(false)

    let missings = null;
    if (props.missing) {
        missings = <div className={styles.indicator} 
                onMouseOver={() => setActive("missing")}   
                onMouseLeave={() => setActive(false)} 
                style={{
                backgroundColor: props.missing.length <= 3 ? "#40b983" : "#ffbd2d",}}>
            {
                active === "missing" ?
                <div className={styles.indicator.open}>
                    <h6 className={styles.needs}>{
                        props.missing.length === 0 ? "Ready to cook!" : "You need"
                    }</h6>
                    <ul className={styles.missList}>
                        {props.missing.map((val, idx) => (
                            <li key={idx}>
                                -&nbsp;&nbsp;{val}
                            </li>
                        ))}
                    </ul>
                </div>
                : props.missing.length
            }


        </div> 
    }

    let expirings = null;
    if (props.expiring) {
        expirings = <div className={styles.indicator} 
            onMouseOver={() => setActive("expiring")}   
            onMouseLeave={() => setActive(false)} 
            style={{
            backgroundColor: "#fd0536",}}>
            {
                active === "expiring" ?
                <div className={styles.indicator.open}>
                    <h6 className={styles.needs}>Close to expiring</h6>
                    <ul className={styles.missList}>
                        {props.expiring.map((val, idx) => (
                            <li key={idx}>
                                -&nbsp;&nbsp;{val}
                            </li>
                        ))}
                    </ul>
                </div>
                : props.expiring.length
            }    

        </div>
    }

    return <div className={styles.indicationBox}>
        {
            active === false || active === "missing" ?
            missings : ""
        }
        {
            active === false || active === "expiring" ?
            expirings : ""
        }
    </div>
    
}