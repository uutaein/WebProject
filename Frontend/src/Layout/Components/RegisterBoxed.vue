<template>
    <div>
        <div class="h-100 bg-premium-dark">
            <div class="d-flex h-100 justify-content-center align-items-center">
                <b-col md="8" class="mx-auto app-login-box">
                    <div id="title">
                        My Asset
                    </div>

                    <div class="modal-dialog w-100">
                        <div class="modal-content">
                            <div class="modal-body">
                                <h5 class="modal-title">
                                    <h4 class="mt-2">
                                        <div>Welcome,</div>
                                        <span>It only takes a <span class="text-success">few seconds</span> to create your account</span>
                                    </h4>
                                </h5>
                                <div class="divider"/>
                                <b-form-group id="exampleInputGroup1"
                                              label-for="exampleInput1"
                                              description="We'll never share your email with anyone else.">
                                    <b-form-input id="exampleInput1"
                                                  type="email"
                                                  required
                                                  v-model="email"
                                                  placeholder="Enter email...">
                                    </b-form-input>
                                </b-form-group>
                                <b-form-group id="exampleInputGroup12"
                                              label-for="exampleInput12">
                                    <b-form-input id="exampleInput12"
                                                  type="text"
                                                  required
                                                  v-model="username"
                                                  placeholder="Enter username...">
                                    </b-form-input>
                                </b-form-group>
                                <div class="row">
                                    <div class="col-md-6">
                                        <b-form-group id="exampleInputGroup2"
                                                      label-for="exampleInput2">
                                            <b-form-input id="exampleInput2"
                                                          type="password"
                                                          required
                                                          v-model="password"
                                                          placeholder="Enter password...">
                                            </b-form-input>
                                        </b-form-group>
                                    </div>
                                    <div class="col-md-6">
                                        <b-form-group id="exampleInputGroup2"
                                                      label-for="exampleInput2">
                                            <b-form-input id="exampleInput2"
                                                          type="password"
                                                          required
                                                          v-model="passwordconfirm"
                                                          placeholder="Repeat password...">
                                            </b-form-input>
                                        </b-form-group>
                                    </div>
                                </div>
                                <div class="divider"/>
                            </div>
                            <div class="modal-footer d-block text-center">
                                <b-button color="primary" class="btn-wide btn-pill btn-shadow btn-hover-shine"
                                          size="lg" @click="signUp">Create Account
                                </b-button>
                            </div>
                        </div>
                    </div>
                    <div class="text-center text-white opacity-8 mt-3">
                        Copyright &copy; ArchitectUI 2019
                    </div>
                </b-col>
            </div>
        </div>
    </div>
</template>

<script>
    import firebase from 'firebase'

    export default {
        name: 'registerBox',
        data(){
            return{
                email:'',
                password:'',
                username:'',
                passwordconfirm:''
            }
        },
        methods:{
            signUp(){
                if(this.passwordconfirm!=this.password) {
                    alert('Check you password again!')
                    return;
                }
                firebase.auth().createUserWithEmailAndPassword(this.email,this.password)
                    .then((user)=>{
                        user.username=this.username;
                        alert('Sign Up success! Welcome  '+user.username);
                        this.email=''
                        this.password=''
                        this.passwordconfirm=''
                        this.username=''
                        this.$router.push('/');
                    })
                    .catch((error)=>{
                        alert(error);
                    })
            }
        }
    }
</script>

<style>
    #title{
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        color: white;
        font-family: Apple;
    }
</style>

