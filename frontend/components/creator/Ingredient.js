import styles from "./Edit.module.scss";



export default function Ingredient(props) {

    return <>
        <div>
            {`${props.ingredient.amount} ${props.ingredient.adjective} ${props.ingredient.ingredient}s`}
        </div>

    </>


}