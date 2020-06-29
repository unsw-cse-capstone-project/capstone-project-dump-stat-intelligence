import * as types from '../types';


export const update_details = (first, last, email, phone) => async dispatch => {
    //Do the actual account rego stuff... 
    let userInfo = {
        first : first,
        last : last, 
        email : email,
        phone : phone
    }
    dispatch({
        type : types.UPDATE_DEETS,
        userInfo : userInfo
    })
}


export const register = (first, last, email, phone, pwd) => async dispatch => {
    //Do the actual account rego stuff... 
    let userInfo = {
        first : first,
        last : last, 
        email : email,
        phone : phone,
        pwd : pwd

    }
    dispatch({
        type : types.LOGIN,
        userInfo : userInfo
    })
}

export const login = (email, pwd) => async dispatch => {
    //DO THE AUTHENTICATION STUFF TO LOGIN
    let userInfo = {
        first : "ronald",
        last  : "mcdonald",
        email : email,
        phone : null,

    }
    dispatch({
        type : types.LOGIN,
        userInfo : userInfo
    })
}

export const logout = () => async dispatch => {
    dispatch({
        type : types.LOGOUT
    })
}