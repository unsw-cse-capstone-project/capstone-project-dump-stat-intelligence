import styles from "./Edit.module.scss";



export default function Ingredient(props) {

    return <>
        <div key={props.idx} className={`tag ${styles.ingredient}`}>
            {`${props.ingredient.amount} ${props.ingredient.unit} ${props.ingredient.adjective ? props.ingredient.adjective : ""} ${props.ingredient.ingredient.name}`}
            <button className={`delete is-small`}/>
        </div>

    </>


}