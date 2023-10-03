import DFINITYCandid;
import Principal;

module {
  type LandRecord = {
    owner: Principal;
    landDetails: Text;
    landID: Nat;
  };
};


  var landRecords : [LandRecord] = [];

  public shared( msg ) func registerLandRecord(owner: Principal, landDetails: Text, landID: Nat) : async () {
    assert (msg.caller == owner, "Only the owner can register land.");
    let landRecord = { owner, landDetails, landID };
    landRecords := Array.append<LandRecord>(landRecords, [landRecord]);
  };

  public query func getLandRecords() : async [LandRecord] {
    return landRecords;
  };
module {

  type User = {
    username: Text;
    passwordHash: Text;
  };

  var users : [User] = [];

  public func registerUser(username: Text, password: Text) : async () {
    assert (isUsernameUnique(username), "Username already exists. Please choose a different username.");

    
    let user = { username, passwordHash = password };
    
    users := Array.append<User>(users, [user]);
  };

  public func login(username: Text, password: Text) : async Bool {
    let user = findUser(username);
    
    
    if (user != null && user.passwordHash == password) {
      return true;
    }
    
    return false;
  };

  private func isUsernameUnique(username: Text) : Bool {
    return Array.every<User>(users, func(user) { user.username != username });
  };

  private func findUser(username: Text) : ?User {
    return Array.find<User>(users, func(user) { user.username == username });
  };

};
module {
  var landRecords : [LandRecord] = [];

  public func registerLand(owner: Principal, landDetails: Text, landID: Nat) : async () {
    if (!isLandIDUnique(landID)) {
      throw Error("Land ID already exists. Please choose a different ID.");
    }

    let landRecord = { owner, landDetails, landID };

    landRecords := Array.append<LandRecord>(landRecords, [landRecord]);
  };

  public query func getLandRecords() : async [LandRecord] {
    return landRecords;
  };

  private func isLandIDUnique(landID: Nat) : Bool {
    for (record in landRecords) {
      if (record.landID == landID) {
        return false; // Land ID already exists
      }
    }
    return true; // Land ID is unique
  };
};