import Link from "next/link";
import styles from "./Cookbook.module.scss";


export default function RecipeIcon(props) {
    return <Link href={`/recipe/${props.id}`}>
        <div className={`card ${styles.recipe}`}>
            <div className="card-image">
                <figure className="image is-4by3">
                    <img src={props.src} alt={props.title}/>
                </figure>
            </div>
            <div className="card-content">
                <h4 className="title is-4">{props.title}</h4>
            </div>
        </div>


    </Link>
}