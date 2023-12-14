

int getName(void) {


    std::string fullname = "/eos/user/s/skkwan/hToAA/condorSkim/2023-11-23-08h21m-benchmark/HZJ_HToWW_Skim.root";

    std::size_t found = fullname.find_last_of("/");
    std::cout << found << std::endl;
    std::string fname = fullname.substr(found + 1);
    
    std::cout << "Getting file name " << fname << std::endl;

    return 0;
}
